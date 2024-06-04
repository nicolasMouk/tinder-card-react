import React, { useState, useEffect } from 'react';
import TinderCard from 'react-tinder-card';

const get_person = 'http://localhost:5000/get_profile';
let index= 0 ;
function get_data() {
    const options = {
        method: 'GET',
        mode: 'cors', // Utiliser 'cors' si le serveur prend en charge les requêtes CORS
        headers: { 
            'Content-Type': 'application/json' 
        }
    };

    return fetch(get_person, options)
        .then(response => {
            if (!response.ok) {
                throw new Error('La requête a échoué.');
            }
            return response.json();
        })
        .then(data => {
            console.log('Réponse :', data);
            return data; // Retourne les données
        })
        .catch(error => {
            console.error('Erreur:', error);
        });
}

function Simple() {
    const [characters, setCharacters] = useState([]);
    useEffect(() => {
        loadProfile();
    }, []);
    const loadProfile = () => {
        get_data().then(data => {
            if (Array.isArray(data)) {
                setCharacters(data);
            } else {
                console.error('Data is not an array:', data);
            }
        });
    };
    const [lastDirection, setLastDirection] = useState();

    const swiped = (direction, nameToDelete) => {
        console.log('removing: ' + nameToDelete);
        setLastDirection(direction);
    };

    const outOfFrame = (name) => {
        index +=1 ;
        console.log(index);
        console.log(characters.length);
        if (index >= characters.length) {
            index=0;
            loadProfile();

        }
    
    };

    return (
        <div>
            <link href='https://fonts.googleapis.com/css?family=Damion&display=swap' rel='stylesheet' />
            <link href='https://fonts.googleapis.com/css?family=Alatsi&display=swap' rel='stylesheet' />
            <h1>The Best Tinder</h1>
            <div className='cardContainer'>
                {characters.map((character) =>
                    <TinderCard className='swipe' key={character.name} onSwipe={(dir) => swiped(dir, character.name)} onCardLeftScreen={() => outOfFrame(character.name)}>
                        <div className='polaroid'>
                            <img src={character.url} alt={character.name} className='photo' />
                            <div className='caption'>
                                <h3>{character.name} {character.age}</h3>
                                <p className='country'>{character.country}</p>
                                <p className='description'>{character.description}</p>
                            </div>
                        </div>
                    </TinderCard>
                )}
            </div>
            
        </div>
    );
}

export default Simple;
