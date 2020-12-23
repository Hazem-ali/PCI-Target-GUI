`timescale 1ns/1ns
`include "clock.v"
`include "verifyAddress.v"
`include "getAddressAndCMD.v"
`include "buffer.v"

module t_buffer2;
reg tframe;
reg[3:0] tCBE;
reg tIRDY;
reg [31:0] tAD;
reg[3:0] operation;

wire [31:0] in_out;
wire tTRDY;
wire tDEVSEL;

parameter READ = 4'b0110;
parameter WRITE = 4'b0111;


//getCMD get2(tframe,tCBE,operation);
assign in_out = (operation==WRITE)? tAD:32'bZ;


initial 
begin
    $dumpfile("testcase1.vcd");
    $dumpvars(0, t_buffer2);
tframe = 1;
tIRDY = 1;
#10

//flag

// // Transaction Begin
// tframe = 0;
// operation=WRITE;
// tCBE = 4'b0111;
// tAD = 32'd1000;
// #10
// tIRDY=0;
// #10

// // Write data
// tCBE=4'b0101;
// tAD=32'hffffffff;
// #10

// tCBE=4'b1111;
// tAD=32'haaaaaaaa;
// #10

// // Transaction end
// tframe = 1;
// tIRDY = 1;
// #10 

// operation=WRITE;
// tframe = 0;
// tCBE = 4'b0110;
// tAD = 32'd1000;
// #10
// tIRDY=0;
// #10

// operation=READ;
// tCBE = 4'b0110;
// #40

$finish;
end



clockGen c1(clk);
buffer B1(clk,tframe,tCBE,in_out,tIRDY,tTRDY,tDEVSEL);



endmodule