import * as React from "react"
import { Avatar, Stack, Typography, TextField, FormControl} from "@mui/material";
import { IconButton, Button} from "@mui/material"

// import Visibility from '@mui/icons-material/Visibility';
// import VisibilityOff from '@mui/icons-material/VisibilityOff';
// import PersonIcon from '@mui/icons-material/Person';

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

    // const [values, setValues] = React.useState({
    //     email: '',
    //     password: '',
    //     userName: '',
    //     age: '',
    //     showPassword: false,
    // });

    // const handleChange = (prop) => (event) => {
    //     setValues({ ...values, [prop]: event.target.value });
    // };
    
    // const handleClickShowPassword = () => {
    //     setValues({
    //         ...values,
    //         showPassword: !values.showPassword,
    //     });
    // };
    
    // const handleMouseDownPassword = (event) => {
    //     event.preventDefault();
    // };


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
            src='https://cdn-icons-png.flaticon.com/512/3135/3135715.png'
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

                // endAdornment = {<InputAdornment position="end">
                //     <PersonIcon />
                // </InputAdornment>}
                />

            <TextField 
                label= 'Password' 
                variant="filled" 
                type="password" 
                sx={{width:'100%', mt: 1}}
                color='warning'
                onChange={(e) => setPassword(e.target.value)}

                // type={values.showPassword ? 'text' : 'password'}
                // value={values.password}
                // // onChange={handleChange('password')}
                // endAdornment={
                // <InputAdornment position="end">
                //     <IconButton
                //     aria-label="toggle password visibility"
                //     onClick={handleClickShowPassword}
                //     onMouseDown={handleMouseDownPassword}
                //     edge="end"
                //     >
                //     {values.showPassword ? <VisibilityOff /> : <Visibility />}
                //     </IconButton>
                // </InputAdornment>
                // }
            />
            <Link href="#" onClick={handleReset} style={{color: 'white', mt:1}}>Forgot Password</Link>

            <Button variant="contained" onClick={handleAction}  sx={{mt:5, backgroundColor: 'white', color: '#223255'}}>Log In</Button>

            <Link to="/signup" style={{color: 'white', mt:2}}>don't have account, Register here</Link>

        </FormControl>

        </Stack>
    )
}