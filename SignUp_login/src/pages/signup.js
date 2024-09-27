import * as React from "react";
import {
  Avatar,
  Stack,
  Typography,
  TextField,
  FormControl,
} from "@mui/material";
import { IconButton, Button } from "@mui/material";
import { Link, useNavigate } from "react-router-dom";
// import Visibility from "@mui/icons-material/Visibility";
// import VisibilityOff from "@mui/icons-material/VisibilityOff";
// import PersonIcon from "@mui/icons-material/Person";
import GoogleIcon from "@mui/icons-material/Google";
import AppleIcon from "@mui/icons-material/Apple";
import FacebookIcon from "@mui/icons-material/Facebook";
import { app, db } from "./Firebase";
import { getAuth, createUserWithEmailAndPassword } from "firebase/auth";
import { useState } from "react";
import { setDoc, doc } from "firebase/firestore";


export default function Sign_Up() {
 
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  
  const handleAction = () => {
    const auth = getAuth();
    console.log("done");
    createUserWithEmailAndPassword(auth, email, password)
      .then((res) => {
        // alert("register successfully")
        
        // navigate("/Home");

        setDoc(doc(db, "users", res.user.uid), {
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
        src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
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
          //   endAdornment={
          //     <InputAdornment position="end">
          //       <PersonIcon />
          //     </InputAdornment>
          //   }
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
          //   endAdornment={
          //     <InputAdornment position="end">
          //       <IconButton
          //         aria-label="toggle password visibility"
          //         onClick={handleClickShowPassword}
          //         onMouseDown={handleMouseDownPassword}
          //         edge="end"
          //       >
          //         {values.showPassword ? <VisibilityOff /> : <Visibility />}
          //       </IconButton>
          //     </InputAdornment>
          //   }
        />

        <Button
          variant="contained"
          sx={{ mt: 5, backgroundColor: "white", color: "#223255" }}
          onClick={handleAction}
        >
          sign up
        </Button>

        <Link to="/login" style={{ color: "white", mt: 2 }}>
          Already have account,
          <br /> Log in here
        </Link>
      </FormControl>
    </Stack>
  );
}
