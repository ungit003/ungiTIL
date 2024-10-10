import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from matplotlib import pyplot as plt

# MNIST 데이터셋 로드
(train_X, train_y), (test_X, test_y) = mnist.load_data()

# 데이터 전처리
train_X = train_X.astype('float32') / 255.0  # Normalize to [0, 1]
test_X = test_X.astype('float32') / 255.0

# 모델 구축
model = models.Sequential()
model.add(layers.Flatten(input_shape=(28, 28)))  # 28x28 이미지를 1D로 변환
model.add(layers.Dense(128, activation='relu'))  # 첫 번째 은닉층
model.add(layers.Dense(10, activation='softmax'))  # 출력층 (10개 클래스)

# 모델 컴파일
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 모델 학습
# epoch = 반복횟수
# batch_size = 를 조절하면서 딥러닝 적합한 가중치 찾아나가는것
model.fit(train_X, train_y, epochs=5, batch_size=32, validation_split=0.2)
'''
epochs = 5
batch_size = 32

for epoch in range(epochs):
    print(f"Epoch {epoch + 1}/{epochs}")
    
    # 전체 데이터셋을 배치 단위로 처리
    for i in range(0, len(train_X_split), batch_size):
        # 배치 데이터 가져오기
        batch_X = train_X_split[i:i + batch_size]
        batch_y = train_y_split[i:i + batch_size]
        
        # 순전파
        with tf.GradientTape() as tape:
            predictions = model(batch_X)
            loss = model.compiled_loss(batch_y, predictions)
        
        # 역전파
        grads = tape.gradient(loss, model.trainable_variables)
        
        # 가중치 업데이트
        model.optimizer.apply_gradients(zip(grads, model.trainable_variables))
        
        # 손실 출력
        if i % (batch_size * 10) == 0:  # 10배치마다 손실 출력
            print(f"Batch {i // batch_size + 1}, Loss: {loss.numpy():.4f}")

    # 검증
    val_predictions = model(val_X_split)
    val_loss = model.compiled_loss(val_y_split, val_predictions)
    val_accuracy = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(val_predictions, axis=1), val_y_split), tf.float32))
    
    print(f"Validation Loss: {val_loss.numpy():.4f}, Validation Accuracy: {val_accuracy.numpy():.4f}")
'''
# 테스트 데이터에 대한 예측
predictions = model.predict(test_X)

# 예측 결과 시각화
num_images = 9  # 시각화할 이미지 수
plt.figure(figsize=(10, 10))
for i in range(num_images):
    plt.subplot(3, 3, i + 1)
    plt.imshow(test_X[i], cmap='gray')
    plt.title(f'Predicted: {np.argmax(predictions[i])}\nTrue: {test_y[i]}')
    plt.axis('off')
plt.tight_layout()
plt.show()
