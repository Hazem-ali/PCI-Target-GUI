module buffer(clk,frame,CBE,AD,IRDY,TRDY,DEVSEL);
// ##### Declaration #####
input clk;
input wire frame;
input wire[3:0] CBE;
inout wire[31:0] AD;
input wire IRDY;
output reg TRDY;
output DEVSEL;

// ##### Define The Operation #####
parameter 
READ = 4'b0110,
WRITE = 4'b0111;

//Counters
reg[2:0] readCount = -1,writeCount =0;
reg[9:0] memCount=0;

reg[31:0] BUFFER[0:3]; //Buffer in the slave
reg[31:0] memory[0:1023]; //Internal Memory for storage;
wire[3:0] operation; //incoming operation from CBE "Command"



// ##### process #####
getCMD get1(frame,CBE,operation);
wire hhh;
verifyAddress verify1(.clk(clk),.frame(frame),.AD(AD),.DEVSEL(DEVSEL),.TRDY(hhh));

always@(hhh)begin
TRDY=hhh;
end

// Tracking writeCount to rise TRDY ((( BUZY )))
always@(negedge clk) begin 

if(writeCount==4) begin 
 TRDY = 1; 
end
if(writeCount==0&&TRDY==1&&DEVSEL==0)begin TRDY=0; end


end

// Transfer Data from buffer when it is fill  ((( TRANSFERING )))
always@(posedge clk) begin 

if(TRDY==1&&writeCount==4) begin 
memory[memCount]<=BUFFER[0];
memory[memCount+1]<=BUFFER[1];
memory[memCount+2]<=BUFFER[2];
memory[memCount+3]<=BUFFER[3];
memCount<=memCount+4;
writeCount=0;
//TRDY=0;
end

end


// Tracking IRDY To making operations
always@(posedge clk) begin 

// Check IRDY To do a Operation
if(IRDY==0&&TRDY==0) begin 
// Make the operation
case(operation)
READ: begin
readCount=readCount+1;
readCount=(readCount==4)? 0:readCount;
end 

WRITE: begin 
BUFFER[writeCount] = {AD[31:24]&{8{CBE[3]}},AD[23:16]&{8{CBE[2]}},AD[15:8]&{8{CBE[1]}},AD[7:0]&{8{CBE[0]}}};
writeCount=writeCount+1;
end
 
default: begin
readCount=readCount+1;
readCount=(readCount==4)? 0:readCount;
end

endcase

end

end

// At Reading ONLY
assign AD = (operation==READ&&TRDY==0&&DEVSEL==0)? BUFFER[readCount]:32'bZ ;




endmodule





