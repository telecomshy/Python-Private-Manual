def plot_history(hist_dict, figsize=(10, 4)):
    fig = plt.figure(figsize=(10, 4))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    loss_values = hist_dict['loss']
    val_loss_values = hist_dict['val_loss']
    epochs = range(1, len(loss_values) + 1)  # 获取横坐标
    ax1.plot(epochs, loss_values, ':bo', label='Training loss')
    ax1.plot(epochs, val_loss_values, ':go', label='Validation loss')
    ax1.set_xlabel('Epochs')
    ax1.set_ylabel('Loss')
    ax1.legend()

    acc = hist_dict['accuracy']
    val_acc = hist_dict['val_accuracy']
    ax2.plot(epochs, acc, ':bo', label='Training acc')
    ax2.plot(epochs, val_acc, ':go', label='Validation acc')
    ax2.set_xlabel('Epochs')
    ax2.set_ylabel('Accuracy')
    ax2.legend()
