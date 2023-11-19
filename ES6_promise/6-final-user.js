import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

async function handleProfileSignup(firstName, lastName, fileName) {
  const userPromise = signUpUser(firstName, lastName)
    .then((value) => ({ status: 'fulfilled', value }))
    .catch((error) => ({ status: 'rejected', value: error }));

  const photoPromise = uploadPhoto(fileName)
    .then((value) => ({ status: 'fulfilled', value }))
    .catch((error) => ({ status: 'rejected', value: error }));

  return Promise.all([userPromise, photoPromise]);
}

export default handleProfileSignup;
