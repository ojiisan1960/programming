-- Ada lesson 3
-- MagPi issue 8
-- Boolean types

with Ada.Text_IO;
use Ada.Text_IO;

procedure Decisions is
    Is_Defective :  Boolean := True;
begin
    if Is_Defective = True then
        Put_Line ("Defective!");
    else
        Put_Line ("Not defective");
    end if;
end Decisions;
