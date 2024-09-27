// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";


// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyDAAJ48iXUB1oqgYoOz5mqm92EW0xwOn_g",
  authDomain: "rightcar4u-ae289.firebaseapp.com",
  projectId: "rightcar4u-ae289",
  storageBucket: "rightcar4u-ae289.appspot.com",
  messagingSenderId: "755491994292",
  appId: "1:755491994292:web:80e19bdb1e93350ad535e1"
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);
export const db = getFirestore(app);