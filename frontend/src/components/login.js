import * as React from "react"
import { Avatar, Stack, Typography, TextField, FormControl} from "@mui/material";
import { IconButton, Button} from "@mui/material"
import img1 from "./singup-login-pic/img1.png"

import GoogleIcon from '@mui/icons-material/Google';
import AppleIcon from '@mui/icons-material/Apple';
import FacebookIcon from '@mui/icons-material/Facebook';
import { Link, useNavigate } from "react-router-dom";

import {
    getAuth,
    signInWithEmailAndPassword,
    sendPasswordResetEmail,
  } from "firebase/auth";
import { useState } from "react";



export default function Log_in(){

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();

    const handleAction = () => {
        const auth = getAuth();
        signInWithEmailAndPassword(auth, email, password)
          .then((res) => {
            // navigate("/home");
            // alert("log in successfully");
          })
          .catch((e) => {
            if (e.code === "auth/wrong-password") {
              // alert("please check the password");
            }
            if (e.code === "auth/user-not-found") {
              // alert("please check the email");
            }
          });
      };
      const handleReset = () => {
        const auth = getAuth();
        sendPasswordResetEmail(auth, email)
          .then(() => {
            // alert("Password reset email sent!") 
            // ..
          })
          .catch((e) => {
            if (e.code === "auth/wrong-password") {
              // alert("please check the password");
            }
            if (e.code === "auth/user-not-found") {
              // alert("please check the email");
            }
          });
      };

    

    return(

        <Stack
        sx = {{height: '100%', border: '3px solid white', borderRadius: '30px 2px', pt: 6}} 
        direction='column'
        alignItems='center'
        alignContent='center'
        justifyContent='center'
        spacing={2}>
            <Avatar
            alt = "account avetar"
            src={img1}
            sx = {{width: 100, height: 100}}
            > </Avatar>
            

            <Typography className="form-header"> LOG IN </Typography>
            
            <FormControl fullWidth sx={{ p: 2, pt: 0 }}>

            <Stack direction='row' justifyContent='center' spacing={2}>
                <IconButton><GoogleIcon sx={{width: 30, height: 30, color: 'rgb(255, 255, 255)'}}/></IconButton>
                <IconButton><AppleIcon sx={{width: 30, height: 30, color: 'rgb(255, 255, 255)'}}/></IconButton>
                <IconButton><FacebookIcon sx={{width: 30, height: 30, color: 'rgb(255, 255, 255)'}}/></IconButton>
            </Stack>
            
            <TextField 
                type= "email" 
                label="Email" 
                variant="filled" 
                color="warning"
                sx={{width:'100%', mt: 1}}
                onChange={(e) => setEmail(e.target.value)}

               
                />

            <TextField 
                label= 'Password' 
                variant="filled" 
                type="password" 
                sx={{width:'100%', mt: 1}}
                color='warning'
                onChange={(e) => setPassword(e.target.value)}

            />
            <Link href="#" onClick={handleReset} style={{color: 'white', mt:1}}>Forgot Password</Link>

            <Button variant="contained" onClick={handleAction}  sx={{mt:5, backgroundColor: 'white', color: '#223255'}}>Log In</Button>

            <Link to="/signup" style={{color: 'white', mt:2}}>don't have account, Register here</Link>

        </FormControl>

        </Stack>
    )
}