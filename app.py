import settings
import model_abstraction_layer
import PIL
import streamlit as st

from pathlib import Path

def reset_on_change():
    st.session_state.selection = '-'

def reset_fields():
    st.session_state.caption = ""
    st.session_state.ground_tokens = ""

# Setting page layout
st.set_page_config(
    page_title="Object Detection with GLIP/DesCo",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page heading
st.title("Object Detection with GLIP/DesCo")

# Sidebar
with st.sidebar:    
    # sidebar header
    st.header('Model Configurations', divider='rainbow')
    st.write("[GLIP](https://github.com/microsoft/GLIP) | [DesCo](https://github.com/liunian-harold-li/DesCo)")
    st.write('Select a Model, then either upload your own image, captions, and ground tokens OR select an example from the "Examples" dropdown menu. Click "Detect Objects" to run.')

    example_options = ["-", "Example 1", "Example 2", "Example 3", "Example 4"]
    valid_options = ["Example 1", "Example 2", "Example 3", "Example 4"]

    model_type = st.radio(
        "Select Model", ['GLIPv2', 'DesCo-GLIP', 'DesCo-FIBER'],
        on_change=reset_on_change)

    text = st.text_input("Caption", key='caption')
    
    if model_type != "GLIPv2":
        ground_tokens = st.text_input("Ground Tokens", key='ground_tokens')
        
    source_img = st.file_uploader(
        "Choose an image...", type=("jpg", "jpeg", "png"),
        on_change=reset_on_change)
    
    selected_example = st.selectbox('Examples', example_options, on_change=reset_fields, key='selection')
    st.divider()

# Selecting Model APIs
if model_type == 'GLIPv2':
    model_api = settings.GLIPV2_URL
elif model_type == 'DesCo-GLIP':
    model_api = settings.DESCO_GLIP_URL
elif model_type == 'DesCo-FIBER':
    model_api = settings.DESCO_FIBER_URL


if model_type == 'GLIPv2':
    col1, col2 = st.columns(2)

    with col1:
        try:
            if source_img is None and selected_example == "-":
                default_image_path = str(settings.DEFAULT_IMAGE)
                default_image = PIL.Image.open(default_image_path)
                st.image(default_image_path, caption="Default Image",
                         use_column_width=True)
            elif selected_example in valid_options:
                image_path = settings.EXAMPLE_CONFIG[model_type][selected_example]["image_path"]
                uploaded_image = PIL.Image.open(image_path)
                text = settings.EXAMPLE_CONFIG[model_type][selected_example]["text"]

                st.image(uploaded_image, caption="Uploaded Image",
                         use_column_width=True)

                with st.sidebar:
                    st.write(f"Example Caption: {text}")
            else:
                uploaded_image = PIL.Image.open(source_img)
                st.image(source_img, caption="Uploaded Image",
                         use_column_width=True)
        except Exception as ex:
            st.error("Error occurred while opening the image.")
            st.error(ex)

    with col2:
        if source_img is None and selected_example == "-":
            default_detected_image_path = str(settings.DEFAULT_DETECT_IMAGE)
            default_detected_image = PIL.Image.open(
                default_detected_image_path)
            st.image(default_detected_image_path, caption='Detected Image',
                     use_column_width=True)
        else:
            if st.sidebar.button('Detect Objects'):
                res = model_abstraction_layer.glipv2_inference(uploaded_image, text)
                st.image(res, caption='Detected Image',
                         use_column_width=True)
elif model_type == 'DesCo-GLIP':
    col1, col2 = st.columns(2)

    with col1:
        try:
            if source_img is None and selected_example == "-":
                default_image_path = str(settings.DEFAULT_IMAGE)
                default_image = PIL.Image.open(default_image_path)
                st.image(default_image_path, caption="Default Image",
                         use_column_width=True)
            elif selected_example in valid_options:
                image_path = settings.EXAMPLE_CONFIG[model_type][selected_example]["image_path"]
                uploaded_image = PIL.Image.open(image_path)
                text = settings.EXAMPLE_CONFIG[model_type][selected_example]["text"]
                ground_tokens = settings.EXAMPLE_CONFIG[model_type][selected_example]["ground_tokens"]

                st.image(uploaded_image, caption="Uploaded Image",
                         use_column_width=True)

                with st.sidebar:
                    st.write(f"Example Caption: {text}")
                    st.write(f"Example Ground Tokens: {ground_tokens}")
            else:
                uploaded_image = PIL.Image.open(source_img)
                st.image(source_img, caption="Uploaded Image",
                         use_column_width=True)
        except Exception as ex:
            st.error("Error occurred while opening the image.")
            st.error(ex)

    with col2:
        if source_img is None and selected_example == "-":
            default_detected_image_path = str(settings.DEFAULT_DETECT_IMAGE)
            default_detected_image = PIL.Image.open(
                default_detected_image_path)
            st.image(default_detected_image_path, caption='Detected Image',
                     use_column_width=True)
        else:
            if st.sidebar.button('Detect Objects'):
                res = model_abstraction_layer.desco_glip_inference(uploaded_image, text, ground_tokens)
                st.image(res, caption='Detected Image',
                         use_column_width=True)
elif model_type == 'DesCo-FIBER':
    col1, col2 = st.columns(2)

    with col1:
        try:
            if source_img is None and selected_example == "-":
                default_image_path = str(settings.DEFAULT_IMAGE)
                default_image = PIL.Image.open(default_image_path)
                st.image(default_image_path, caption="Default Image",
                         use_column_width=True)
            elif selected_example in valid_options:
                image_path = settings.EXAMPLE_CONFIG[model_type][selected_example]["image_path"]
                uploaded_image = PIL.Image.open(image_path)
                text = settings.EXAMPLE_CONFIG[model_type][selected_example]["text"]
                ground_tokens = settings.EXAMPLE_CONFIG[model_type][selected_example]["ground_tokens"]

                st.image(uploaded_image, caption="Uploaded Image",
                         use_column_width=True)
                
                with st.sidebar:
                    st.write(f"Example Caption: {text}")
                    st.write(f"Example Ground Tokens: {ground_tokens}")
            else:
                uploaded_image = PIL.Image.open(source_img)
                st.image(source_img, caption="Uploaded Image",
                         use_column_width=True)
        except Exception as ex:
            st.error("Error occurred while opening the image.")
            st.error(ex)

    with col2:
        if source_img is None and selected_example == "-":
            default_detected_image_path = str(settings.DEFAULT_DETECT_IMAGE)
            default_detected_image = PIL.Image.open(
                default_detected_image_path)
            st.image(default_detected_image_path, caption='Detected Image',
                     use_column_width=True)
        else:
            if st.sidebar.button('Detect Objects'):
                res = model_abstraction_layer.desco_fiber_inference(uploaded_image, text, ground_tokens)
                st.image(res, caption='Detected Image',
                         use_column_width=True)
else:
    st.error("Please select a valid source type!")
