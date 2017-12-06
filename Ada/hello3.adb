-- Ada_Programming 
-- http://en.wikibooks.org/wiki/Ada_Programming/Basic
-- hello world 2

with Ada.Text_IO;               -- Text IO package

procedure Hello3 is
    package IO renames Ada.Text_IO; -- alias IO to Ada.Text_IO
begin
    IO.Put_Line("Hello World!");
    IO.New_Line;
    IO.Put_Line("I am an Ada program with package use");
end Hello3;
