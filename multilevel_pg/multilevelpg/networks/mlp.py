
import tensorflow as tf
# from malib.utils.keras import PicklableKerasModel
from multilevel_pg.multilevelpg.utils.keras import PicklableKerasModel

def MLP(input_shapes,
        output_size,
        hidden_layer_sizes,
        activation='relu',
        output_activation='linear',
        preprocessors=None,
        name='mlp',
        *args,
        **kwargs):
    inputs = [
        tf.keras.layers.Input(shape=input_shape)
        for input_shape in input_shapes
    ]

    if preprocessors is None:
        # print("preprocessor is None!!")
        preprocessors = (None, ) * len(inputs)

    preprocessed_inputs = [
        preprocessor(input_) if preprocessor is not None else input_
        for preprocessor, input_ in zip(preprocessors, inputs)
    ]

    concatenated = tf.keras.layers.Lambda(
        lambda x: tf.concat(x, axis=-1)
    )(preprocessed_inputs)

    # print(concatenated.shape())

    out = concatenated
    for units in hidden_layer_sizes:
        out = tf.keras.layers.Dense(
            units, *args, activation=activation, use_bias=True,**kwargs
        )(out)

    out = tf.keras.layers.Dense(
        output_size, *args, activation=output_activation, use_bias=True, **kwargs
    )(out)

    model = PicklableKerasModel(inputs, out, name=name)

    return model