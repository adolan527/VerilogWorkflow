//
// Created by Aweso on 12/28/2024.
//

#ifndef TESTBENCH_MODULE_H
#define TESTBENCH_MODULE_H

#include <vector>
#include <string>
#include <cstring>
#include <algorithm>

#define LINEBUFFERSIZE 1024
#define NAMEBUFFERSIZE 32

enum Direction{
    Input = 0,
    Output = 1
};


struct Port{
    int width;
    Direction dir;
    std::string name;

    Port(int w, Direction d, std::string &n){
        width = w; dir = d; name = n;
    }
};

enum Encoding{
    UTF8 = 0,
    UTF16LE = 1
};

class Module {
    std::vector<Port> m_Ports;
    std::string m_name;
public:
    void Print(){
        printf("Name: %s\n",m_name.c_str());
        for(auto &p : m_Ports){
            printf("%s, %s, %d\n",p.name.c_str(),p.dir==Input?"Input":"Output",p.width);
        }
    }

    void CreateTestBench(FILE *fstream){
        std::vector<Port*> inputs, outputs;
        bool clock = false;
        for(auto &p: m_Ports){
            if(p.dir==Input) inputs.push_back(&p);
            else outputs.push_back(&p);
        }
        std::sort(inputs.begin(), inputs.end(),[](Port *a, Port *b) {
            return a->width < b->width;
        });

        std::sort(outputs.begin(), outputs.end(),[](Port *a, Port *b) {
            return a->width < b->width;
        });

        int lastWidth = 0;
        for(auto &i : inputs){
            bool firstOnLine = false;
            if(i->width!=lastWidth){
                firstOnLine = true;
                if(lastWidth!=0) fprintf(fstream,";\n");
                lastWidth = i->width;
                if(lastWidth!=1) fprintf(fstream,"reg[%d:0]",lastWidth-1);
                else fprintf(fstream,"reg",lastWidth-1);
            }
            fprintf(fstream,"%c %s",firstOnLine ? ' ' : ',',i->name.c_str());
        }
        fprintf(fstream,";\n");
        lastWidth = 0;
        for(auto &o : outputs){
            if(o->width!=lastWidth){
                if(lastWidth!=0) fprintf(fstream,";\n");
                lastWidth = o->width;
                if(lastWidth!=1) fprintf(fstream,"wire[%d:0]",lastWidth-1);
                else fprintf(fstream,"wire",lastWidth-1);
            }
            fprintf(fstream," %s",o->name.c_str());
        }
        fprintf(fstream,";\n");

        fprintf(fstream,"\n%s %s_inst(\n",m_name.c_str(),m_name.c_str());
        bool firstPort = true;
        for(auto &p: m_Ports){
            if(p.name=="clk") clock = true;
            fprintf(fstream,"%c.%s(%s)",firstPort ? ' ' : ',',p.name.c_str(),p.name.c_str());
            firstPort = false;
        }
        fprintf(fstream,");\n");
        if(clock) fprintf(fstream,"\nalways #5 clk = ~clk;\n");
        fprintf(fstream,"\ninitial begin\n");
        if(clock) fprintf(fstream,"clk = 0;\n");
        fprintf(fstream,"end\n");


    }


    Module(std::string &filename, std::string &fileEncoding){
        Encoding encoding = UTF8;
        if(fileEncoding=="UTF8") encoding = UTF8;
        else if(fileEncoding=="UTF16LE") encoding = UTF16LE;
        FILE *file = fopen(filename.c_str(),"r");
        if(!file) return;
        {
            char firstLine[LINEBUFFERSIZE] = {0};
            char name[NAMEBUFFERSIZE] = {0};
            char *ptr, *nameptr;
            nameptr = name;
            fgets_encoding(firstLine,64,file,encoding);
            ptr = strstr(firstLine, "module");
            if (!ptr) return;
            ptr += sizeof("module");
            while (isblank(*ptr))ptr++;
            while (*ptr != '(' && !isblank(*ptr)) {
                *nameptr++ = *ptr++;
            }
            m_name = name;
        }
        while(!feof(file)){
            char lineBuffer[LINEBUFFERSIZE] = {0};
            char *ptr;

            Direction lineDir;
            int lineWidth = 1;
            std::vector<std::string> names;

            fgets_encoding(lineBuffer, LINEBUFFERSIZE, file,encoding);

            //identifies in or out
            ptr = strstr(lineBuffer, "input");
            if(ptr) lineDir = Input;
            else{
                ptr = strstr(lineBuffer, "output");
                if(ptr) lineDir = Output;
                else break;
            }

            ptr += lineDir == Input ? sizeof("input")-1: sizeof("output")-1;//skips over input or output

            while(isblank(*ptr))ptr++;//skips whitespace

            if(lineDir==Output){ //skips over reg if it is an output
                auto temp = strstr(ptr,"reg");
                if(ptr==temp){
                    ptr+=sizeof("reg")-1;
                }
                while(isblank(*ptr))ptr++;//skips whitespace

            }

            if(*ptr=='['){//identifies and skips width
                int upper, lower;
                sscanf(ptr,"[%d:%d]",&upper,&lower);
                lineWidth += upper-lower;
                while(*ptr!=']')ptr++;
                ptr++;
                while(isblank(*ptr))ptr++;//skips whitespace
            }

            while(ptr!=lineBuffer+LINEBUFFERSIZE-1){
                char nameBuffer[NAMEBUFFERSIZE] = {0};
                sscanf(ptr,"%s",nameBuffer);
                int length = strlen(nameBuffer);
                if(length==0 || nameBuffer[0]=='/')break;
                if(nameBuffer[0]!=',') {
                    if(nameBuffer[length-1]==',')nameBuffer[length-1]=0;
                    names.emplace_back(nameBuffer);
                    ptr+=length;
                }
                else ptr++;
            }

            for(auto &n : names){
                m_Ports.emplace_back(lineWidth,lineDir,n);
            }



        }
        fclose(file);

    }
private:
    void fgets_encoding(char *buffer, size_t maxCount, FILE *file, Encoding fileEncoding){
        switch(fileEncoding){
            case UTF8:
                fgets(buffer,maxCount,file);
                break;
            case UTF16LE:
                for(int i = 0; i < maxCount; i++){
                    char temp = fgetc(file);
                    if(!temp) i--;
                    else{
                        if(temp=='\n' || feof(file)){
                            buffer[i] = 0;
                            break;
                        }
                        else{
                            buffer[i] = temp;
                        }
                    }
                }
        }
    }

};


#endif //TESTBENCH_MODULE_H
