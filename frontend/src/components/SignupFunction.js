import * as React from "react";
import { useState } from "react";

import { Link, useNavigate } from "react-router-dom";

// MUI Imports
import {
  Avatar,
  Stack,
  Typography,
  TextField,
  FormControl,
} from "@mui/material";
import { IconButton, Button } from "@mui/material";
import GoogleIcon from "@mui/icons-material/Google";
import AppleIcon from "@mui/icons-material/Apple";
import FacebookIcon from "@mui/icons-material/Facebook";

// Firebase Imports
import { auth, database } from "../firebase";
import { createUserWithEmailAndPassword } from "firebase/auth";
import { setDoc, doc } from "firebase/firestore";

// Images
import img1 from '../images/img1.png'


export default function Sign_Up() {
 
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  
  const handleAction = () => {
    console.log("done");
    createUserWithEmailAndPassword(auth, email, password)
      .then((res) => {
        // alert("register successfully")
        
        // navigate("/Home");

        setDoc(doc(database, "users", res.user.uid), {
          email: email,
          password: password,
          userId:res.user.uid
        }).then(() => {
          console.log("done2");
        });
      })
        .catch((error) => {
          if (error.code === "auth/wrong-password") {
        //   toast.error("Please check the Password");
        // alert("Please check the Password")
        }
        if (error.code === "auth/user-not-found") {
          // alert("Please check the Email");
        }
        });
  };

  return (
    <Stack
      sx={{
        height: "100%",
        border: "3px solid white",
        borderRadius: "30px 2px",
        pt: 6,
      }}
      direction="column"
      alignItems="center"
      alignContent="center"
      justifyContent="center"
      spacing={2}
    >
      
      <Avatar
        alt="account avetar"
        src={img1}
        sx={{ width: 100, height: 100 }}
      >
        {" "}
      </Avatar>
      
      <Typography className="form-header"> SIGN UP </Typography>

      <FormControl fullWidth sx={{ p: 2, pt: 0 }}>
        <Stack direction="row" justifyContent="center" spacing={2}>
          <IconButton>
            <GoogleIcon
              sx={{ width: 30, height: 30, color: "rgb(255, 255, 255)" }}
            />
          </IconButton>
          <IconButton>
            <AppleIcon
              sx={{ width: 30, height: 30, color: "rgb(255, 255, 255)" }}
            />
          </IconButton>
          <IconButton>
            <FacebookIcon
              sx={{ width: 30, height: 30, color: "rgb(255, 255, 255)" }}
            />
          </IconButton>
        </Stack>

        <TextField
          type={"text"}
          label="Full Name"
          //   onChange={(e) => setName(e.target.value)}
          variant="filled"
          color="warning"
          sx={{ width: "100%" }}
        />

        <TextField
          type="email"
          label="Email"
          onChange={(e) => setEmail(e.target.value)}
          variant="filled"
          color="warning"
          sx={{ width: "100%", mt: 1 }}
          
        />

        <TextField
          label="Password"
          variant="filled"
          type="password"
          sx={{ width: "100%", mt: 1 }}
          color="warning"
          //   type={values.showPassword ? "text" : "password"}
          //   value={values.password}
          onChange={(e) => setPassword(e.target.value)}
          
        />

        <Button
          variant="contained"
          sx={{ mt: 5, backgroundColor: "white", color: "#223255" }}
          onClick={handleAction}
        >
          Sign up
        </Button>

        <Link to="/login" style={{ color: "white", mt: 2 }}>
          Already have account,
          <br /> Log in here
        </Link>
      </FormControl>
    </Stack>
  );
}
