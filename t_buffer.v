module buffertestbench;
reg tframe;
reg[3:0] tCBE;
reg tIRDY;
reg [31:0] tAD;
reg operation;

wire [31:0] in_out;
wire tTRDY;


parameter READ = 1;
parameter WRITE = 0;

assign in_out = (operation == WRITE) ? tAD : 32'bZ;


initial 
begin
tframe = 1;
tIRDY = 1;

#10 
tframe = 0;
tIRDY = 0;
tCBE = 4'b0111;
operation = WRITE;


tAD = 32'd287;
#10

tAD = 32'd1000;
#10

tAD = 32'd133;
#10

tAD = 32'd176;
#10

tAD = 32'haa;
#20

tAD = 32'hbb;
#10

tAD = 32'hcc;
#10

tAD = 32'hdd;
#10

tAD = 32'hee;
#20

tframe = 1;
tIRDY = 1;


#10
tframe = 0;
tIRDY = 0;
tCBE = 4'b0110;
operation = READ;


end



clockGen c1(clk);
buffer B1(clk, tframe, tCBE, in_out, tIRDY, tTRDY);



endmodule
