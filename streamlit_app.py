import streamlit as st
import pandas as pd
import itertools

# Function to generate permutations between factions
def generate_permutations(df):
    factions = df['Faction'].dropna().tolist()
    permutations = list(itertools.permutations(factions, 2))
    permutations_df = pd.DataFrame(permutations, columns=["Faction", "Other_Faction"])
    return permutations_df

# Streamlit UI
st.title("Faction Permutations Generator")

# Upload CSV file
uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Display the first few rows of the uploaded file
    st.write("Uploaded CSV preview:")
    st.write(df.head())
    
    # Generate permutations
    permutations_df = generate_permutations(df)
    
    # Display the permutations
    st.write("Generated Permutations:")
    st.write(permutations_df)
    
    # Provide a download button for the generated CSV
    csv = permutations_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Permutations as CSV",
        data=csv,
        file_name='permutations_factions.csv',
        mime='text/csv',
    )
