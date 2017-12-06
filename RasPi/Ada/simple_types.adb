-- Ada lesson 2
-- MagPi issue 6
-- Ada types

with Ada.Text_IO;
use Ada.Text_IO;

procedure Simple_Types is
    X   :   integer := 10;
    Y   :   constant integer := 20;
    Result:     integer := 0;
begin
    Result := X + Y ;

    Put_Line ("X = " & integer'image(X));
    Put_Line ("Y = " & integer'image(Y));
    Put_Line ("Result = " & integer'image(Result));
end Simple_Types;

