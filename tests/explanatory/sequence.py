def explanatory_sequence(
    *,
    model_factory,
    model_null,
    p_values,
    rejection_region,
    plot_fn,
    style,
    save_pattern: str | None = None,
):
    """
    Explanatory sequence:
    - model_null: fixes Nullmodell (H0)
    - model_factory: erzeugt alternative Modelle (H1)
    """
    for i, p in enumerate(p_values):
        model_alt = model_factory(p)

        save = None
        if save_pattern is not None:
            save = save_pattern.format(i=i, p=p)

        plot_fn(
            model_alt=model_alt,
            model_null=model_null,
            rejection_region=rejection_region,
            style=style,
            save=save,
        )
