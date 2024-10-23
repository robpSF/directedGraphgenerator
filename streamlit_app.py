import streamlit as st
import pandas as pd
import itertools

# Function to generate permutations between factions and add affinity
def generate_permutations(selected_factions):
    permutations = list(itertools.permutations(selected_factions, 2))
    # Create DataFrame and add a default affinity value
    permutations_df = pd.DataFrame(permutations, columns=["Faction", "Other_Faction"])
    permutations_df['Affinity'] = 0  # Default affinity value; modify if needed
    return permutations_df

# Streamlit UI
st.title("Faction Permutations Generator with Affinity")

# Upload CSV file
uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Display the first few rows of the uploaded file
    st.write("Uploaded CSV preview:")
    st.write(df.head())
    
    # Let the user select factions to remove
    try:
        factions = df['Faction'].dropna().tolist()
    except:
        st.write("The column 'Faction' is missing from the uploaded file. Please ensure that your file contains a column named 'Faction' and try again.")
        exit
    
    selected_factions = st.multiselect("Select factions to include (unselect to remove):", factions, default=factions)
    
    if selected_factions:
        # Generate permutations with affinity
        permutations_df = generate_permutations(selected_factions)
        
        # Display the permutations
        st.write("Generated Permutations with Affinity:")
        st.write(permutations_df)
        
        # Provide a download button for the generated CSV
        csv = permutations_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Permutations with Affinity as CSV",
            data=csv,
            file_name='permutations_factions_with_affinity.csv',
            mime='text/csv',
        )
    else:
        st.write("Please select at least two factions to generate permutations.")
