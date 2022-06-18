import obspython as obs
import pytesseract

def script_description():
  return """<center><h2>Source To Text!!</h2></center>
            <p>Turn a source in the current scene into text.</p>"""

# Fills the given list property object with the names of all sources plus an empty one
def populate_list_property_with_source_names(list_property):
  sources = obs.obs_enum_sources()
  obs.obs_property_list_clear(list_property)
  obs.obs_property_list_add_string(list_property," ", "")
  for source in sources:
    name = obs.obs_source_get_name(source)
    obs.obs_property_list_add_string(list_property, name, name)
  obs.source_list_release(sources)

def script_properties():
  props = obs.obs_properties_create()

  # Drop-down list of sources
  list_property = obs.obs_properties_add_list(props, "source_name", "Source name",
                    obs.OBS_COMBO_TYPE_LIST, obs.OBS_COMBO_FORMAT_STRING)
  populate_list_property_with_source_names(list_property)
  obs.obs_properties_add_text(props, "source_name", "Source name", obs.OBS_TEXT_DEFAULT)

  list_property2 = obs.obs_properties_add_list(props,"output_text", "Output text",
                    obs.OBS_COMBO_TYPE_LIST, obs.OBS_COMBO_FORMAT_STRING)
  populate_list_property_with_source_names(list_property2)
  obs.obs_properties_add_text(props, "output_text", "Output text", obs.OBS_TEXT_DEFAULT)

  # Button to refresh the drop-down list
  obs.obs_properties_add_button(props, "button", "Refresh list of sources",
    lambda props,prop: True if populate_list_property_with_source_names(list_property) else True)

  return props

def script_defaults(settings):
  obs.obs_data_set_default_string(settings, "source_name", "")
  obs.obs_data_set_default_string(settings, "output_text", "")


def script_tick(seconds):
  current_scene_as_source = obs.obs_frontend_get_current_scene()
  if current_scene_as_source:
    current_scene = obs.obs_scene_from_source(current_scene_as_source)
    scene_item = obs.obs_scene_find_source_recursive(current_scene,source_name)
    #if scene_item:
        #f = open('C:/Users/annie/Desktop/img_text.txt', mode = 'w')
        #text = 'pytesseract.pytesseract.image_to_string(scene_item)'
        #f.write(text)
    obs.obs_source_release(current_scene_as_source)

def script_update(settings):
  global source_name, frequency, amplitude
  current_scene_as_source = obs.obs_frontend_get_current_scene()
  if current_scene_as_source:
    current_scene = obs.obs_scene_from_source(current_scene_as_source)
    scene_item = obs.obs_scene_find_source_recursive(current_scene,source_name)
    if scene_item:
      obs.obs_sceneitem_set_rot(scene_item, 0 )
    obs.obs_source_release(current_scene_as_source)
  source_name = obs.obs_data_get_string(settings, "source_name")
