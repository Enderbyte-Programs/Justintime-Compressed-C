release:
	pyinstaller --onefile jcc.py
	cp ./dist/jcc .
install:
	cp ./jcc /usr/bin
clean:
	rm ./jcc
	rm -rf ./dist
	rm -rf ./build
uninstall:
	rm /usr/bin/jcc