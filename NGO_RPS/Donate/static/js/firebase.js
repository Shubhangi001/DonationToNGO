
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/9.1.1/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.1.1/firebase-analytics.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyCKuXMBgHP5uyb_vdPYOwVgR54_YCugzAU",
    authDomain: "donatengo-c090d.firebaseapp.com",
    projectId: "donatengo-c090d",
    storageBucket: "donatengo-c090d.appspot.com",
    messagingSenderId: "768173708267",
    appId: "1:768173708267:web:b545d4d3a3004f2e8d3fae",
    measurementId: "G-5VBTGBRFNN"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);
