

base.txt:
	docker build . -t sample-stack-base:bionic --target base
	echo $(date) > base.txt

run.txt: base.txt
	docker build . -t sample-stack-run:bionic --target run
	echo $(date) > run.txt

build.txt: base.txt
	docker build . -t sample-stack-build:bionic --target build
	echo $(date) > build.txt

build-app: build.txt
	pack build sample-app --path samples/apps/java-maven --builder cnbs/sample-stack-build:bionic

