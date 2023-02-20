import React, { useState, useEffect } from 'react';
import axios from 'axios';

function User() {
  const [username, setUser] = useState(null);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/user/')
      .then(response => {
        setUser(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  if (User) {
    return (
      <div>
        <p>Username: {User.username}</p>
      </div>
    );
  } else {
    return <p>Loading...</p>;
  }
}

export default User;
