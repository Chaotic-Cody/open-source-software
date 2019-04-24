# Installing and building Lua5.2 for cross compilation with Windows using mingw

1. Download the [Lua 5.2.4 source code](https://www.lua.org/ftp/lua-5.2.4.tar.gz)

2. Extract the .tar and .gz files to a known directory using your favorite file extraction tool (I use [7-Zip](https://www.7-zip.org/download.html))

3. Change the cc compiler flag in the Makefile (located in lua5.2.4/src) from gcc to x86_64-w64-mingw32-gcc (64 bit minGW compiler)

4. Run make mingw in the lua-5.2.4 directory

5. Remove the .exe extension from lua.exe and luac.exe in the src/lua directory using

   "mv src/lua.exe src/lua"
  
   "mv src/luac.exe src/luac"

6. Run make local to move all library info into lua-5.2.4/install

##### Author: Cody Messina 4/23/2019