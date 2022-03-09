import requests
from utilities.configuration import getConfig
from utilities.payload import JSON

key = getConfig()['API']['keyword']


# Add places
def test_AddAddress():
    addURL = getConfig()['API']['endpoint'] + getConfig()['API']['addResource']
    response = requests.post(url=addURL, params={'key': key}, json=JSON.addJson)
    assert 200 == response.status_code
    details = response.json()
    place_ID = details['place_id']
    assert "OK" == details['status']
    return place_ID


# get details of existing place
def test_GetAddress():
    getURL = getConfig()['API']['endpoint'] + getConfig()['API']['getResource']
    details = requests.get(url=getURL, params={
        'key': key,
        'place_id': test_AddAddress()
    })
    assert 200 == details.status_code


# # update existing place with new values
def test_UpdateAddress():
    update_URL = getConfig()['API']['endpoint'] + getConfig()['API']['updateResource']
    update = requests.put(url=update_URL,
                          params={
                              'key': key,
                              'place_id': test_AddAddress()
                          },
                          json={
                              "place_id": test_AddAddress(),
                              "address": JSON.updateAddress,
                              "key": key
                          })
    assert 200 == update.status_code


# Delete existing place
def test_DelAddress():
    delURL = getConfig()['API']['endpoint'] + getConfig()['API']['delResource']
    delete = requests.delete(url=delURL, params={'key': key}, json={"place_id": test_AddAddress()})
    assert 200 == delete.status_code
    print(delete.text)
