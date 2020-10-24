//Requirements Importer
let { PythonShell } = require("python-shell")
const J2Url = require("j2url")
const Express = require("express")
const Chalk = require("chalk")

//Variables
const Port = process.env.PORT || 8176
const Web = Express()
const Args = process.argv.slice(2)

//Express
Web.get("/", function(req, res){
    var username = J2Url.getParam(req.originalUrl, "user")
    var password = J2Url.getParam(req.originalUrl, "pass")
    console.log(username + " " + password)
    var options = {
        args: ['--username', username, '--password', password]
    }
    PythonShell.run("./resources/index.py", options, function(err, stdout){
        if(err){
            console.log(Chalk.red("[FBStrike-GToken] Invalid username or password."))
            return
        }
        try{
            stdout = stdout.toString()
            if(stdout.indexOf("Error") != -1){
                res.json({
                    "error": "Invalid username or password."
                })
            }else{
                res.json({
                    "success": stdout
                })
            }
        }catch{
            res.json({
                "error": "Invalid username or password."
            })
        }
    })
})
Web.listen(Port, ()=>{
console.log(`=============================
    Server Status: Online
    Port: ${Port}
=============================`)
})