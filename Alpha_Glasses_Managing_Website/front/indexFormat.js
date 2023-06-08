const fs = require('fs');
const path = require('path');

const HTML = () => {
  const directoryPath = path.join(__dirname, '../users'); //__dirname 특별한 변수로 현재 디렉토리를 나타냄 이걸 사용한 이유는 6번째 줄에서 directoryPath 절대경로만 받기 때문.
  let users = fs.readdirSync(directoryPath);
  let userListHTML = "";
  users.forEach(user => {
    if(user != "style.css" && user != "list") userListHTML = `${userListHTML} <li class="userListElement"><a href="/user/${user}">${user}</a></li>`;
  });

  return `
  <html>
    <head>
      <meta charset="utf-8">
		  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		  <meta name="viewport" content="width=device-width, initial-scale=1.0">
		  <title>
		  	Alpha Glasses
		  </title>
		  <link rel="icon" href="../images/Alpha_Black.png" type="image/x-icon" />
		  <meta name="keywords" content="" />
		  <meta name="description" content="" />
		  <link href="http://fonts.googleapis.com/css?family=Source+Sans+Pro:200,300,400,600,700,900" rel="stylesheet" />
		  <link href="../default.css" rel="stylesheet" type="text/css" media="all" />
	  	<link href="../fonts.css" rel="stylesheet" type="text/css" media="all" />
    </head>
    <body>
      <div id="header-wrapper">
			  <div id="header" class="container">
				  <div id="logo">
					  <h1><a href="../index.html">Alpha Glasses</a></h1>
					  <span>Hidden page <a href="../hidden.html" rel="nofollow">Alpha</a></span>
				  </div>
				  <div id="menu">
				    <ul>
				  	  <li><a href="../index.html" accesskey="1" title="">Homepage</a></li>
				  	  <li><a href="../about.html" accesskey="3" title="">About Us</a></li>
				  	  <li><a href="../user/list" accesskey="2" title=""><strong>Upload Files</strong></a></li>
				  	  <li><a href="../how.html" accesskey="4" title="">How to Use</a></li>
				  	  <li><a href="#contact" accesskey="5" title="">Contact Us</a></li>
				    </ul>
				  </div>
			  </div>
		  </div>
		  <div id="wrapper1">
        <div id="welcome" class="container">
          <div class="title">
          <a style="font-size: 50" class="bnt" href="../program/Alpha_Camera_Application.zip" download>대상 사진 촬영 프로그램</a>
          </div>
          <div class="title">
  			  	<h2>대상 리스트</h2>
  			  </div>
          <p style="font-size: 24px; text-align: center;">
            사용자가 저장한 대상들 입니다. <br>
            이제 여기서 대상을 추가하시거나 추가된 대상을 수정하실 수 있습니다.
				  </p>
          <br>
          <br>
          <br>
          ${userListHTML}
          <form action="../api/addUser" method="post">
            <input id="userInput" type="text" name="name" id="name">
            <input id="buttonAdd" type="submit" value="추가">
          </form>
          
        </div>
      </div>
      <div id="wrapper4">
        <div id="footer" class="container">
          <div>
            <header class="title">
              <h2 id="contact">Contact Us</h2>
              <span class="byline">Contact to direct Alpha's social account if you want to have conversation with him.</span> 
            </header>
            <ul class="contact">
              <li><a href="https://www.instagram.com/0____alpha____0/" class="icon icon-instagram"><span>Instagram</span></a></li>
              <li><a href="https://www.facebook.com/Alpha-754036214939107" class="icon icon-facebook"><span>Facebook</span></a></li>
              <li><a href="https://github.com/Alpha-Dvlp" class="icon icon-github"><span>GitHub</span></a></li>
            </ul>
          </div>
        </div>
      </div>
    </body>
  </html>
  `;
}

module.exports = {
  HTML
}