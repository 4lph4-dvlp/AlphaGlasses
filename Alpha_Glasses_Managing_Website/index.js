const express = require('express');
const fs = require('fs');
const path = require('path');
const multer = require('multer');
const bodyParser = require('body-parser'); //파싱 문자열을 가공하기 쉽게 바꿔주는 역할 을 하는 라이브러리

const app = express();
const port = 80;

const indexFormat = require('./front/indexFormat');
const userFormat = require('./front/userFormat');

app.use(bodyParser.json()); 
app.use(bodyParser.urlencoded({ extended: true }));
app.use('/static', express.static('users'));

app.get('/user/list', (req, res) => { //indexFormat.js 를 호출하는 것
  res.send(indexFormat.HTML());
});

app.get('/user/:userName', (req, res) => { //UserFormat를 호출하는 것
  res.send(userFormat.HTML(req.params.userName));
});


app.post('/api/user/:userName/info', (req, res) => { //수정하거나 보낸 텍스트를 텍스트파일로 바꾸는 것
  let userName = req.params.userName;
  let dir = `./users/${userName}/info.txt`;
  let newInfo = req.body.info;
  fs.writeFile(dir, newInfo, (err) => {
    if(err) console.log(err);
    res.redirect('/user/list');
  });
});

app.post('/api/user/:userName/upload', (req, res) => { //사진을 업로드하는 곳인데 여기서 대용량 파일을 다루는 Multer 라이브러리가 사용됨
  var fileName = 1;
  let userName = req.params.userName;
  let storage = multer.diskStorage({
    destination: (req, file, cb) => {
      cb(null, `./users/${userName}/img`);
    },
    filename: (req, file, cb) => {
      cb(null, `${fileName++}` + path.extname(file.originalname));
    }
  });
  let upload = multer({storage}).array('profile', 200); //multer를 사용하여 함수 생성

  upload(req, res, (err) => {
    if(err) console.log(err);
    res.redirect('/user/list');
  });
});

app.post('/api/addUser', (req, res) => { //새로운 대상을 추가하는 것
  let name = req.body.name;
  let dir = `./users/${name}`;

  if (!fs.existsSync(dir)){
    fs.mkdirSync(dir);
    fs.mkdirSync(`${dir}/img`);
    fs.writeFile(`${dir}/info.txt`, "", (err) => {
      if(err) console.log(err);
    });
    fs.appendFile(`./users/list`, `${encodeURIComponent(name)}\n`, (err) => {
      if(err) console.log(err);
      res.redirect('/user/list');
    });
  }
});

app.get('/test', (req, res) => { //테스트 코드 입니다.
  res.sendFile(path.join(__dirname + "/front/html/inputs.html"));
});

app.get('/', (req, res) => { //index.html을 불러오는 것
  res.sendFile(path.join(__dirname + "/home/index.html"));
})

app.use('/', express.static('home'));

app.listen(port, () => { //콘솔에 연결됬다는 로그를 보낸다.
  console.log(`Example app listening at http://localhost:${port}`);
});
