module verifyAddress(clk,frame,AD,DEVSEL,TRDY);

//##### Decleration #####
parameter deviceAddress = 1000; //Specific address for a device

input wire clk;
input wire frame;
input wire[31:0] AD;
output reg DEVSEL;
output reg TRDY;
reg [2:0] counter=0;
reg [2:0] elCounterElTany=0;
reg[31:0] recievedAddress;


//##### Process #####

always@(negedge clk)begin

if(frame==1)begin 
if(elCounterElTany<=3)begin 
elCounterElTany=elCounterElTany+1;
end


if(elCounterElTany==3)begin
DEVSEL = 1 ; //Active LOW
TRDY = 1; //Active LOW
counter=0;
end

end

end

always@(AD)begin 
if(counter==1)begin
recievedAddress=AD;
end

end


always@(negedge clk) begin 
if(frame==0)begin
 
/*if(counter==0)begin 
recievedAddress=AD;
end*/

if(counter<=3)begin 
counter=counter+1;
end


if(counter==3) begin
DEVSEL = (recievedAddress==deviceAddress)? 0:1 ; //Active LOW
TRDY = (recievedAddress==deviceAddress)? 0:1 ; //Active LOW


end

end


end


endmodule

