import nemo.collections.asr as nemo_asr
import pathlib, random, os

BASE_PATH = str(pathlib.Path(__file__).parent.resolve())
MODEL_NAME = "Model-uz.nemo"
MODEL_PATH = os.path.join(BASE_PATH, MODEL_NAME)

quartznet = nemo_asr.models.EncDecCTCModel.restore_from(restore_path=MODEL_PATH)

def save_file(audio):
    random.randint(0, 1000)
    complete_path = os.path.join(BASE_PATH, str(random.randint(0, 1000)) + audio.filename)
    data = audio.stream.read()
    file = open(complete_path, "wb")
    file.write(data)
    return complete_path


def delete_file(filename):
    os.remove(filename)

def transcribe(audio):
    filename = save_file(audio)
    result = quartznet.transcribe([filename])[0]
    delete_file(filename)
    return result

