import { useState } from 'react';
import './App.css';

function App() {
  const [race, setRace] = useState('human');
  const [charClass, setCharClass] = useState('fighter');
  const [tone, setTone] = useState('neutral');
  const [npc, setNpc] = useState('');

  const generateNpc = async () => {
    const params = new URLSearchParams({ race, char_class: charClass, tone });
    const res = await fetch(`http://localhost:8000/npc?${params.toString()}`);
    const data = await res.json();
    setNpc(data.npc);
  };

  return (
    <div className="app">
      <h1>Storysmith NPC Generator</h1>
      <label>
        Race:
        <input value={race} onChange={(e) => setRace(e.target.value)} />
      </label>
      <label>
        Class:
        <input value={charClass} onChange={(e) => setCharClass(e.target.value)} />
      </label>
      <label>
        Tone:
        <input value={tone} onChange={(e) => setTone(e.target.value)} />
      </label>
      <button onClick={generateNpc}>Generate</button>
      <pre>{npc}</pre>
    </div>
  );
}

export default App;