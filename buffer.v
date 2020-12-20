module buffer(clk,frame,CBE,AD,IRDY,TRDY);
// ##### Declaration #####
input clk;
input wire frame;
input wire[3:0] CBE;
inout wire[31:0] AD;
input wire IRDY;
output reg TRDY;

// ##### Define The Operation #####
parameter 
READ = 4'b0110,
WRITE = 4'b0111;

//Counters
reg[2:0] readCount = 0,writeCount =0;
reg[9:0] memCount=0;

reg[31:0] BUFFER[0:3]; //Buffer in the slave
reg[31:0] memory[0:1023]; //Internal Memory for storage;
wire[3:0] operation; //incoming operation from CBE "Command"



// ##### process #####
getCMD get1(.frame(frame),.AD(AD),.CBE(CBE),.CMD(operation)); //get Command and put it in operation

// Tracking writeCount to rise TRDY ((( BUSY )))
always@(negedge clk) begin 

if(writeCount==4) begin 
 TRDY = 1;
 tempCount=0; 
end
if(writeCount==0)begin TRDY=0; end


end

// Transfer Data from buffer when it is fill  ((( TRANSFERING )))
always@(posedge clk) begin 

if(TRDY==1 && writeCount==4) begin
memory[memCount] <= BUFFER[0];
memory[memCount+1] <= BUFFER[1];
memory[memCount+2] <= BUFFER[2];
memory[memCount+3] <= BUFFER[3];
memCount <= memCount + 4;
writeCount = 0;
end

end


// Tracking IRDY To making operations
always@(posedge clk) begin 

// Check IRDY To do a Operation
if(IRDY == 0 && TRDY == 0) begin 
// Make the operation
case(operation)
READ: begin
readCount=readCount+1;
readCount=(readCount==4)? 0:readCount;
end 

WRITE: begin 
BUFFER[writeCount] = AD;
writeCount=writeCount+1;
end
 
default: ; //Feh default hnaaa 

endcase

end

end

// At Reading ONLY
assign AD = (operation==READ)? BUFFER[readCount]:32'bZ ;


endmodule





