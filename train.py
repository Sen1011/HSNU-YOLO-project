from ultralytics import YOLO
import comet_ml

project_name = "expirement"

comet_ml.login(project_name=project_name)

# Load a pretrain model
model = YOLO("yolo11n.pt")

# Training
results = model.train(
    # Train settings, about: https://docs.ultralytics.com/modes/train/#train-settings
    data=None,
    epochs=100,
    time=None,
    patience=100,
    batch=16,
    imgsz=640,
    save=True,
    save_period=-1,
    cache=False,
    device=None,
    workers=8,
    project=project_name,
    name=None,
    exist_ok=False,
    pretrained=True,
    optimizer='auto',
    seed=0,
    deterministic=True,
    single_cls=False,
    classes=None,
    rect=False,
    multi_scale=False,
    cos_lr=False,
    close_mosaic=10,
    resume=False,
    amp=True,
    fraction=1.0,
    profile=False,
    freeze=None,
    lr0=0.01,
    lrf=0.01,
    momentum=0.937,
    weight_decay=0.0005,
    warmup_epochs=3.0,
    warmup_momentum=0.8,
    warmup_bias_lr=0.1,
    box=7.5,
    cls=0.5,
    dfl=1.5,
    pose=12.0,
    kobj=2.0,
    nbs=64,
    overlap_mask=True,
    mask_ratio=4,
    dropout=0.0,
    val=True,
    plots=False,

    #Augmentation Settings and Hyperparameters, about: https://docs.ultralytics.com/modes/train/#augmentation-settings-and-hyperparameters
    hsv_h=0.015,
    hsv_s=0.7,
    hsv_v=0.4,
    degrees=0.0,
    translate=0.1,
    scale=0.5,
    shear=0.0,
    perspective=0.0,
    flipud=0.0,
    fliplr=0.5,
    bgr=0.0,
    mosaic=1.0,
    mixup=0.0,
    copy_paste=0.0,
    copy_paste_mode='flip',
    auto_augment='randaugment',
    erasing=0.4,
    crop_fraction=1.0)