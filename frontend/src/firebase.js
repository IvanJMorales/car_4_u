import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getFirestore } from "firebase/firestore";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries
// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional

const firebaseConfig = {
  apiKey: "AIzaSyAN8SzJ9oUDpBNtmAse9CfSg0M4HlCKUNY",
  authDomain: "car4u-dd0c1.firebaseapp.com",
  databaseURL: "https://car4u-dd0c1-default-rtdb.firebaseio.com",
  projectId: "car4u-dd0c1",
  storageBucket: "car4u-dd0c1.appspot.com",
  messagingSenderId: "391542669703",
  appId: "1:391542669703:web:326fbaf5d96b58c0379322",
  measurementId: "G-L6PL878E6X"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

// Initialize Cloud Firestore and get a reference to the service
export const database = getFirestore(app);

