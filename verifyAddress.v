module verifyAddress(AD,DEVSEL,TRDY);

//##### Decleration #####
parameter deviceAddress = 1000; //Specific address for a device
inout wire[31:0] AD;
output wire DEVSEL;
output wire TRDY;

//##### Process #####
assign DEVSEL = (AD==deviceAddress)? 0:1 ; //Active LOW
assign TRDY = (AD==deviceAddress)? 0:1 ; //Active LOW

endmodule

