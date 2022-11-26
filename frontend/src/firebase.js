import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getFirestore } from "firebase/firestore";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries
// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional

const firebaseConfig = {

  apiKey: "AIzaSyDMEH9kvb4HdeUBhDVnjIlzkoxp9UatiXI",

  authDomain: "car4u-2.firebaseapp.com",

  databaseURL: "https://car4u-2-default-rtdb.firebaseio.com",

  projectId: "car4u-2",

  storageBucket: "car4u-2.appspot.com",

  messagingSenderId: "766140858814",

  appId: "1:766140858814:web:33b934072b3b7f3dc1b9ef",

  measurementId: "G-FCSQZB2331"

};


// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

// Initialize Cloud Firestore and get a reference to the service
export const database = getFirestore(app);

