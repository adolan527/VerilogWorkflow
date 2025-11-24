
def generate_complex_multiplier(A, B):
    template = f"""
cmpy_0 x_complex_multiplier_{A}_{B} (
  .aclk(clk),                              // input wire aclk
  .aresetn(reset_n),                       // input wire aresetn
  .aclken(clken),                           // input wire aclken

  .s_axis_a_tvalid(s_axis_a_tvalid),        // input wire s_axis_a_tvalid
  .s_axis_a_tready(s_axis_a_tready_{A}_{B}), // output wire s_axis_a_tready
  .s_axis_a_tdata(channel_{A}_base),        // input wire [31 : 0] s_axis_a_tdata

  .s_axis_a_tuser(s_axis_tuser),            // input wire [0 : 0] s_axis_a_tuser
  .s_axis_a_tlast(s_axis_tlast),            // input wire s_axis_a_tlast

  .s_axis_b_tdata(channel_{B}_conj),        // input wire [31 : 0] s_axis_b_tdata
  .s_axis_b_tready(s_axis_b_tready_{A}_{B}), // output wire s_axis_b_tready
  .s_axis_b_tvalid(s_axis_b_tvalid),        // input wire s_axis_b_tvalid

  .s_axis_b_tuser(s_axis_tuser),            // input wire [0 : 0] s_axis_b_tuser
  .s_axis_b_tlast(s_axis_tlast),            // input wire s_axis_b_tlast

  .m_axis_dout_tvalid(m_axis_dout_tvalid_{A}_{B}),  // output wire m_axis_dout_tvalid
  .m_axis_dout_tdata(next_result_matrix_{A}_{B}),    // output wire [63 : 0] m_axis_dout_tdata

  .m_axis_dout_tready(m_axis_dout_tready),  // input wire m_axis_dout_tready
  .m_axis_dout_tuser(m_axis_dout_tuser_{A}_{B}),    // output wire [1 : 0] m_axis_dout_tuser
  .m_axis_dout_tlast(m_axis_dout_tlast_{A}_{B})   // output wire m_axis_dout_tlast
);
    """
    return template.strip()

def portAssignment(A,B):
    template = f"""
    s_axis_a_tready_{A}_{B} & 
    """
    return template.strip()

# Example usage
A = "0"
B = "0"
#print(generate_complex_multiplier(A, B))

for a in range(0,4):
    for b in range(0,4):
        print(portAssignment(a, b))

