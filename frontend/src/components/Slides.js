import "../styles/style.css";
import React from "react";
import Grid from "@mui/material/Grid";
import CssBaseline from "@mui/material/CssBaseline";
import { Slide } from "react-slideshow-image";
import "react-slideshow-image/dist/styles.css";
import Log_in from "./login";
import img2 from "../images/img2.png";
import img3 from "../images/img3.png";
import img4 from "../images/img4.png";
import img5 from "../images/img5.png";
import img6 from "../images/img6.png";

const buttonStyle = {
  width: "25px",
  background: "none",
  border: "0px",
};

const properties = {
  prevArrow: (
    <button style={{ ...buttonStyle }}>
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="#fff">
        <path d="M242 180.6v-138L0 256l242 213.4V331.2h270V180.6z" />
      </svg>
    </button>
  ),
  nextArrow: (
    <button style={{ ...buttonStyle }}>
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="#fff">
        <path d="M512 256L270 42.6v138.2H0v150.6h270v138z" />
      </svg>
    </button>
  ),
};

export default function Index() {
  const images = [{ img2 }, { img3 }, { img4 }, { img5 }, { img6 }];

  return (
    <Grid container component="main" sx={{ height: "100vh" }}>
      <CssBaseline />

      <Grid
        item
        xs={false}
        sm={5}
        md={8}
        sx={{
          backgroundImage:
            {img5},
          backgroundColor: (t) =>
            t.palette.mode === "light"
              ? t.palette.grey[50]
              : t.palette.grey[900],
          backgroundSize: "cover",
          backgroundPosition: "center",
        }}
      >
        <Slide {...properties}>
          <div className="each-slide-effect">
            <div
              style={{
                backgroundImage: `url(${img2})`,
                height: "100vh",
                width: "100%",
                backgroundSize: "cover",
                backgroundPosition: "center",
              }}
            ></div>
          </div>
          <div className="each-slide-effect">
            <div
              style={{
                backgroundImage: `url(${img3})`,
                height: "100vh",
                width: "100%",
                backgroundSize: "cover",
                backgroundPosition: "center",
              }}
            ></div>
          </div>
          <div className="each-slide-effect">
            <div
              style={{
                backgroundImage: `url(${img4})`,
                height: "100vh",
                width: "100%",
                backgroundSize: "cover",
                backgroundPosition: "center",
              }}
            ></div>
          </div>
          <div className="each-slide-effect">
            <div
              style={{
                backgroundImage: `url(${img5})`,
                height: "100vh",
                width: "100%",
                backgroundSize: "cover",
                backgroundPosition: "center",
              }}
            ></div>
          </div>
          <div className="each-slide-effect">
            <div
              style={{
                backgroundImage: `url(${img6})`,
                height: "100vh",
                width: "100%",
                backgroundSize: "cover",
                backgroundPosition: "center",
              }}
            ></div>
          </div>
        </Slide>
      </Grid>

      <Grid item xs={12} sm={7} md={4} sx={{ padding: 5, height: "100vh" }}>
        <div className="index-circle-top"></div>

        <Log_in />
      </Grid>
    </Grid>
  );
}
