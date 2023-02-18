import React, { useState, useEffect} from 'react'

export  function prueba() {
  const[data, setData] = useState(null);

  useEffect(() => {
    fetch('/api')
        .then(response => response.json())
        .then(data => setData(data));
  }, []);

  if (!data) {
    return <div>Cargando...</div>;
  }

  return (
    <div>
      <h1>puta el weon ordinario</h1>
    </div>
  )
}

export default prueba;
