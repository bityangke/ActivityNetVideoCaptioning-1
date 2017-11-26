from lstm_decoder import *


def build_model(model_config):
    model = LSTMDecoder(model_config, mode="inference")
    model.build()


def load_model_params(sess, model_path):
    saver = tf.train.Saver()
    saver.restore(sess, model_path)


def feed_image(sess, input_features):
    initial_state = sess.run(fetches="lstm/initial_state:0",
                             feed_dict={"input_features:0": input_features})
    return initial_state


def inference_step(sess, input_feed, state_feed):
    softmax_output, state_output = sess.run(
        fetches=["softmax:0", "lstm/state:0"],
        feed_dict={
            "input_feed:0": input_feed,
            "lstm/state_feed:0": state_feed,
        })
    return softmax_output, state_output