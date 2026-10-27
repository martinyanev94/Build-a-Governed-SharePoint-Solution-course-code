import { BaseClientSideWebPart } from '@microsoft/sp-webpart-base';

export interface INorthstarStatusWebPartProps {
  title: string;
}

export default class NorthstarStatusWebPart extends BaseClientSideWebPart<INorthstarStatusWebPartProps> {
  public render(): void {
    const title = this.properties.title || 'Northstar status';
    this.domElement.innerHTML = `
      <section class="northstar-status">
        <h2>${title}</h2>
        <p>Ready for portal data.</p>
      </section>`;
  }
}
