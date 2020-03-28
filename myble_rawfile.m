clear all
data= xlsread ('ecg.xlsx') ;
i=1;
j=1;
while (i<15)
a=blelist;
list=a.Address;
for j=1:size(list)
if(list(j)=="3403DE436DD5")
b = ble("3403DE436DD5");
c = characteristic(b,"FFE0","FFE1");
x=data(i,2);
write(c,int2str(x))
data(i,2)
i=i+1
clear b
pause(1)
end

end
end

