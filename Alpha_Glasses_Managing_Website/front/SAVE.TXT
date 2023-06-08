const fs = require('fs');
const path = require('path');

const HTML = (userName) => {
  const directoryPath = path.join(__dirname, `../users/${userName}`);

  if(fs.existsSync(directoryPath)) {
    let userInfo = fs.readFileSync(`${directoryPath}/info.txt`);
    
    return `
    <html>
      <head>
        <meta charset="utf-8">
      </head>
      <body>
        <form><a href="../">↩️</a></form>
        <form action="../api/user/${userName}/upload" method="post" enctype="multipart/form-data">
          <input type="file" name="profile" multiple="multiple">
          <input type="submit">
        </form>
        <form action="../api/user/${userName}/info" method="post">
          <textarea name="info" id="" cols="30" rows="10">${userInfo}</textarea>
          <input type="submit">
        </form>
      </body>
    </html>
    `;
  } else {
    return `
    <html>
      <head>
        <meta charset="utf-8">
      </head>
      <body>
        Nothing here;
      </body>
    </html>      
    `;
  }
}

module.exports = {
  HTML
}