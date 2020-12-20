module getCMD(frame,AD,CBE,CMD);
// ##### Declaration #####
input wire frame;
input wire[31:0] AD;
input wire[3:0] CBE;
output reg[3:0] CMD;

// ##### process #####
always@(negedge frame) begin 
CMD <= CBE;
end

endmodule 