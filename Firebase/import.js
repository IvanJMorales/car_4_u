import { initializeFirebaseApp } from 'firestore-export-import'

import serviceAccount from './car4ukey.json'

// If you want to pass settings for firestore, you can add to the options parameters
const options = {
  firestore: {
    host: 'localhost:8080',
    ssl: false,
  },
}

// Initiate Firebase App
// appName is optional, you can omit it.
const appName = '[DEFAULT]'
initializeFirebaseApp(serviceAccount, appName, options)

// the appName & options are OPTIONAL
// you can initalize the app without them
// initializeFirebaseApp(serviceAccount)