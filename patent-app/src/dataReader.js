var fs = require('fs');

var data = [];

function readData(){
    fs.readFile('./patent-app/src/data/data.txt',(err, fileData) => {
        if (err) throw err;
        var lines = fileData.toString().split('\n');
        for (var i = 0; i < lines.length; i++) {
            var datas = lines[i].split(': ');
            if(datas[0] === 'Inventors'){
                data.inventors = datas[1];
            }
            else if (datas[0] === 'Name'){
                data.name = datas[1];
            }
            else if (datas[0] === 'PatentNum'){
                data.num = datas[1];
            }
            else if (datas[0] === 'Country of orgin'){
                data.country = datas[1];
            }
            else if (datas[0] === 'Status'){
                data.status = datas[1];
            }
            else if (datas[0] === 'Current Company assignee'){
                data.company = datas[1];
            }
        }
    });
}
readData();

export default data;