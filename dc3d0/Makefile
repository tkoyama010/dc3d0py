dc3d0.so : dc3d0_wrapper.o DC3D.o
	gcc -shared -o $@ $< DC3D.o -lgfortran
dc3d0_wrapper.o : dc3d0_wrapper.c
	gcc -Wall -fPIC -c $<
DC3D.o: DC3D.f
	gcc -Wall -fPIC -c $< -lgfortran
install:
	make
	cp dc3d0.so /usr/lib/
uninstall:
	rm /usr/lib/dc3d0.so
clean:
	rm *.o *.so
