## Postman Scripts For Validating Security Headers + Not No Secure Security Headers

HTTP Security Headers should be present in all the responses whether its a web application or API at bare minimum.

A lot of time we perform an assessment and recommend security headers. Developers configure these and while revalidation we observe them not to be in place again. Well, you have to validate everything and report back? Why not automate it for the Postman Collections? 

So, there should a simple Postman Test which can enable the developers configure and then test APIs on their own end to ensure everything is in place. 

The following postman test does the same work. 

## 1. Usage

- For each API, add the below script in the Tests section.
- Open up the console in postman.
- Submit the request.
- Validate the results in the console. 
- In case script doesn't work as intended, well you can troubleshoot.
- While also feel free to add more tests to the same or revamp the script to a better one by creating a pull request. 

## 2. Headers Supported

The below scripts checks for the following headers. 

1. Server Header
2. X-Powered-By Header
3. X-AspNet-Version Header
4. X-AspNetMvc-Version
5. X-Content-Type-Options Header
6. X-Frame-Options Header
7. Cache-Control Header
8. Strict-Transport-Security Header
9. X-XSS-Protection Header
10. Content-Security-Policy Header

## 3. In Working

![Usage](https://raw.githubusercontent.com/deFr0ggy/deFr0ggy.github.io/master/assets/bloggers/usage.jpeg)

## 4. Postman Test Script

```
// Author - Kamran Saifullah - deFr0ggy
// August 1st, 2023
// @CyDefOps, @Project-KillChain, 
// https://twitter.com/@deFr0ggy
// https://linkedin.com/in/KamranSaifullah
// https://github.com/CyDefOps/project-killchain/
// https://cydefops.com


// Below Headers Should Not Be Present


pm.test("Checking Server Header", function () {
        if (pm.response.headers.get("Server")) {
            console.warn("Remove The Server Header!");
        } else {
           console.info("Server header is not present - Its Good!!!") 
        }
    });

pm.test("Checking X-Powered-By Header", function () {
        if (pm.response.headers.get("X-Powered-By")) {
            console.warn("Remove The X-Powered-By Header");
        } else {
            console.info("X-Powered-By header is not present - Its Good!!!")
        }
    });

pm.test("Checking X-AspNet-Version Header", function () {
        if (pm.response.headers.get("X-AspNet-Version")) {
            console.warn("Remove The X-AspNet-Version Header");
        } else {
            console.info("X-AspNet-Version header is not present - Its Good!!!")
        }
    });

pm.test("Checking X-AspNetMvc-Version Header", function () {
        if (pm.response.headers.get("X-AspNetMvc-Version")) {
            console.warn("Remove The X-AspNetMvc-Version Header");
        } else {
            console.info("X-AspNetMvc-Version header is not present - Its Good!!!")
        }
    });


// Below are the Mandatory Headers

pm.test("Checking X-Content-Type-Options Header", function () {
     if(pm.response.headers.get("X-Content-Type-Options")) {
        console.info("X-Content-Type-Options Header is Set - Its Good!!!")
     
    } else {
        console.warn("X-Content-Type-Options Header is NOT SET!")   
    }
    });

pm.test("Checking X-XSS-Protection Header", function () {
     if(pm.response.headers.get("X-XSS-Protection")) {
        console.info("X-XSS-Protection Header is Set - Its Good!!!")
        
    } else {
        console.warn("X-XSS-Protection Header is NOT SET!")
    }
    });

pm.test("Checking X-Frame-Options Header", function () {
     if(pm.response.headers.get("X-Frame-Options")) {
        console.info("X-Frame-Options Header is Set - Its Good!!!")
        
    } else {
        console.warn("X-Frame-Options Header is NOT SET!")
    }
    });


pm.test("Checking Content-Security-Policy Header", function () {
    if(pm.response.headers.get("Content-Security-Policy")) {
        console.info("Content-Security-Policy Header is Set - Its Good!!!")
        
    } else {
        console.warn("Content-Security-Policy Header is NOT SET!")
    }
    });

pm.test("Checking Cache-Control Header", function () {
    if(pm.response.headers.get("Cache-Control")) {
        console.info("Cache-Control Header is Set - Its Good!!!")
    } else {
       
        console.warn("Cache-Control Header is NOT SET!")
    }
    });

pm.test("Checking Strict-Transport-Security Header", function () {
    if(pm.response.headers.get("Strict-Transport-Security")) {
        console.info("Strict-Transport-Security Header is Set - Its Good!!!")
    } else {
        
        console.warn("Strict-Transport-Security Header is NOT SET!")
    }
    });
```
