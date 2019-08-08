var name = null;
var email = null;
  function onSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
    name = profile.getName();
    console.log('Image URL: ' + profile.getImageUrl());
    email = profile.getEmail(); // This is null if the 'email' scope is not present.
    window.location="/setupinfo"

  }
  // function signOut() {
  //   var auth2 = gapi.auth2.getAuthInstance();
  //   auth2.signOut().then(function () {
  //     console.log('User signed out.');
  //   });
  // }
