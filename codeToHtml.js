hljs = require('highlight.js')
fs = require('fs')

//includeJS('highlight.js/highlight.js')
if (process.argv.length > 2) {
	filename = process.argv[2]
	
	
	
	fd = fs.openSync(filename, 'r');
		
	l = fs.statSync(filename).size
	buf = new Buffer(l);
	n = fs.readSync(fd, buf, 0, l, null);
	
	
	if (process.argv.length > 3) {
		language = process.argv[3]	
	} else {
		extension = filename.split('.').slice(-1)[0];
		switch (extension) {
		case 'js':
			language = 'javascript'
			break;
		default:
			language = null;
			break;
		}
	}
	
	if (language == null) {
		console.log(hljs.highlightAuto(buf.toString()).value)
	} else {
		console.log(hljs.highlight(language, buf.toString()).value);
	}
	
	//n = fs.writeSync(fd, buf, 0, buf.length, null)
	//console.log(fs.readdirSync('.'))
	
	//console.log(hljs.highlight('Python', 'for i in range(10): print i').value);
}

