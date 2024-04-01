import streamlit as st
import pandas as pd


import streamlit as st



# Function to display the upload data page
def upload_data_page():
    # Capture the CSV file
    st.header("Please upload your CSV file here:");
    data = st.file_uploader("Upload CSV file",type="csv");
    if data:
        df = pd.read_csv(data)
        st.dataframe(df.head(5))  # Display the first few rows of the dataframe
        st.divider()

        # Create dropdowns for SP, PV, MV
        columns = df.columns.tolist()
        selected_sp = st.selectbox("Please Select Setpoint Tag:", columns)
        columns.remove(selected_sp)

        selected_pv = st.selectbox("Please Select Process Variable Tag:", columns)
        columns.remove(selected_pv)

        selected_mv = st.selectbox("Please Select Controller Output Tag:", columns)
        columns.remove(selected_mv)

        selected_sv = st.selectbox("Please Select State variable Tag:", columns)


        # Show state variable
        st.divider()
        st.write(f"Selected Setpoint Tag: {selected_sp}")
        st.write(f"Selected Process Variable Tag: {selected_pv}")
        st.write(f"Selected Controller Output Tag: {selected_mv}")        
        st.write(f"Selected State Variable Tag: {selected_sv}")        


# Function to display the input thresholds page
def connect_database_placeholder():
    st.header("Connect to Database")
    st.write("This is a place holder for Connect to Database ingestion")


# Function to display the metrics report page
def live_stream_placeholder():
    st.header("Live Stream Data")
    st.write("This is a place holder for Live Stream Data ingestion")


# Main app
def main():
    st.sidebar.title("Data Input Options")
    selection = st.sidebar.radio("Go to", ["Upload CSV file", "Connect to Database", "Live Stream Data"])

    if selection == "Upload CSV file":
        #st.write('Hi')
        upload_data_page()
    elif selection == "Connect to Database":
        connect_database_placeholder()
    elif selection == "Live Stream Data":
        live_stream_placeholder()


if __name__ == "__main__":
    main()


# def main():
#     #load_dotenv()

#     st.header("Automatic Controller Assesment Tool")

#     # Create a sample dataframe
#     data = {
#         'Category': ['line_1_rougher_1_froth_velocity_sp', 'line_1_rougher_2_froth_velocity_sp', 'line_1_rougher_3_froth_velocity_sp', 'SP...'],
#         'Subcategory': ['Apple', 'Carrot', 'Banana', 'Beef']
#     }
#     df = pd.DataFrame(data)

#     # Create the primary dropdown for Category
#     selected_category = st.selectbox("Please choose the Set point tag that you are interested to investigate:", df['Category'].unique())

#     # Filter the dataframe based on the selected category
#     filtered_df = df[df['Category'] == selected_category]

#     # Create a dictionary for dependent dropdown options
#     dependent_dropdown_options = {
#         'options': filtered_df['Subcategory'].unique().tolist(),
#         'default': None  # You can set a default value here if needed
#     }

#     # Display the dependent dropdown using st_aggrid
#     # grid_options = GridOptionsBuilder.from_dataframe(filtered_df).build()
#     # AgGrid(filtered_df, gridOptions=grid_options, data_editor=dependent_dropdown_options)


#     #Capture user input
#     st.write("Based on your selection, Following are corresponding PV and MV:")
#     user_input = st.text_input("🔍")

#     if user_input:

#         response= 'Hello'  #get_answer(relavant_docs,user_input)
#         st.write(response)

        
#         #Button to create a ticket with respective department
#         button = st.button("Submit ticket?")

#         #if button:
#             #Get Response



# if __name__ == '__main__':
#     main()



