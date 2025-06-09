import streamlit as st
import datetime

# General shelf-life data (in days) for more common foods
SHELF_LIFE = {
    'fridge': {
        'milk': 7,
        'eggs': 21,
        'chicken': 2,
        'beef': 3,
        'pork': 3,
        'fish': 2,
        'cheese': 14,
        'lettuce': 7,
        'apple': 30,
        'banana': 7,
        'grapes': 7,
        'strawberry': 3,
        'leftovers': 4,
    },
    'freezer': {
        'chicken': 180,
        'beef': 365,
        'pork': 180,
        'fish': 90,
        'bread': 90,
        'vegetables': 365,
        'fruits': 365,
    },
    'pantry': {
        'bread': 5,
        'potatoes': 30,
        'onions': 30,
        'apple': 21,
        'banana': 5,
        'cereal': 180,
        'rice': 365,
    }
}

def get_shelf_life(food, location):
    location = location.lower()
    food = food.lower()
    if location in SHELF_LIFE and food in SHELF_LIFE[location]:
        return SHELF_LIFE[location][food]
    return None

st.title('🥗 Food Spoilage Checker')
st.write('Check the freshness and spoilage risk of your stored food!')

food = st.text_input('What food item did you store?')
storage_date = st.date_input('When did you store it?', value=datetime.date.today())
location = st.selectbox('Where did you store it?', ['Fridge', 'Freezer', 'Pantry'])

if st.button('Check Spoilage Risk'):
    if not food:
        st.warning('Please enter a food item.')
    else:
        shelf_life = get_shelf_life(food, location)
        if shelf_life is None:
            st.error(f"Sorry, I don't have shelf-life data for {food} in the {location.lower()}.")
        else:
            today = datetime.date.today()
            days_stored = (today - storage_date).days
            days_left = shelf_life - days_stored
            expiration_date = storage_date + datetime.timedelta(days=shelf_life)

            st.write(f"**Stored on:** {storage_date}")
            st.write(f"**Today:** {today}")
            st.write(f"**Estimated expiration date:** {expiration_date}")

            if days_left < 0:
                st.error(f"❌ RED: Warning! Your {food} stored in the {location.lower()} is likely spoiled! It expired {-days_left} days ago.")
            elif days_left == 0:
                st.warning(f"⚠️ YELLOW: Caution! Your {food} stored in the {location.lower()} expires today!")
            elif days_left <= 2:
                st.warning(f"⚠️ YELLOW: Heads up! Your {food} stored in the {location.lower()} will expire in {days_left} day(s). Use it soon!")
            else:
                st.success(f"✅ GREEN: Your {food} stored in the {location.lower()} is fresh. {days_left} day(s) left until spoilage.") 